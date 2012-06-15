%global cartridgedir %{_libexecdir}/stickshift/cartridges/ruby-1.9

Summary:   Provides ruby rack support running on Phusion Passenger
Name:      cartridge-ruby-1.9
Version: 0.1.4
Release:   1%{?dist}
Group:     Development/Languages
License:   ASL 2.0
URL:       http://openshift.redhat.com
Source0: http://mirror.openshift.com/pub/crankcase/source/%{name}/%{name}-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: git
Requires:  stickshift-abstract
Requires:  rubygem(stickshift-node)
Requires:  mod_bw
Requires:  sqlite-devel
Requires:  libev
Requires:  libev-devel
Requires:  rubygems
Requires:  ruby193-rubygems
Requires:  ruby193
Requires:  ruby193-js
Requires:  ruby193-js-devel
Requires:  ruby193-libyaml
Requires:  ruby193-libyaml-devel
Requires:  ruby193-ruby
Requires:  ruby193-ruby-devel
Requires:  ruby193-ruby-irb
Requires:  ruby193-ruby-libs
Requires:  ruby193-ruby-tcltk
Requires:  ruby193-rubygem-ZenTest
Requires:  ruby193-rubygem-actionmailer
Requires:  ruby193-rubygem-actionpack
Requires:  ruby193-rubygem-activemodel
Requires:  ruby193-rubygem-activerecord
Requires:  ruby193-rubygem-activeresource
Requires:  ruby193-rubygem-activesupport
Requires:  ruby193-rubygem-arel
Requires:  ruby193-rubygem-bacon
Requires:  ruby193-rubygem-bcrypt-ruby
Requires:  ruby193-rubygem-bigdecimal
Requires:  ruby193-rubygem-bson
Requires:  ruby193-rubygem-builder
Requires:  ruby193-rubygem-bundler
Requires:  ruby193-rubygem-coffee-rails
Requires:  ruby193-rubygem-coffee-script
Requires:  ruby193-rubygem-diff-lcs
Requires:  ruby193-rubygem-erubis
Requires:  ruby193-rubygem-execjs
Requires:  ruby193-rubygem-fakeweb
Requires:  ruby193-rubygem-fssm
Requires:  ruby193-rubygem-hike
Requires:  ruby193-rubygem-http_connection
Requires:  ruby193-rubygem-i18n
Requires:  ruby193-rubygem-introspection
Requires:  ruby193-rubygem-io-console
Requires:  ruby193-rubygem-journey
Requires:  ruby193-rubygem-jquery-rails
Requires:  ruby193-rubygem-json
Requires:  ruby193-rubygem-json_pure
Requires:  ruby193-rubygem-mail
Requires:  ruby193-rubygem-metaclass
Requires:  ruby193-rubygem-mime-types
Requires:  ruby193-rubygem-minitest
Requires:  ruby193-rubygem-mocha
Requires:  ruby193-rubygem-mongo
Requires:  ruby193-rubygem-multi_json
Requires:  ruby193-rubygem-polyglot
Requires:  ruby193-rubygem-rack
Requires:  ruby193-rubygem-rack-cache
Requires:  ruby193-rubygem-rack-ssl
Requires:  ruby193-rubygem-rack-test
Requires:  ruby193-rubygem-rails
Requires:  ruby193-rubygem-railties
Requires:  ruby193-rubygem-rake
Requires:  ruby193-rubygem-rdoc
Requires:  ruby193-rubygem-rspec
Requires:  ruby193-rubygem-ruby2ruby
Requires:  ruby193-rubygem-ruby_parser
Requires:  ruby193-rubygem-sass
Requires:  ruby193-rubygem-sass-rails
Requires:  ruby193-rubygem-sexp_processor
Requires:  ruby193-rubygem-sinatra
Requires:  ruby193-rubygem-sprockets
Requires:  ruby193-rubygem-sqlite3
Requires:  ruby193-rubygem-test_declarative
Requires:  ruby193-rubygem-thor
Requires:  ruby193-rubygem-tilt
Requires:  ruby193-rubygem-treetop
Requires:  ruby193-rubygem-tzinfo
Requires:  ruby193-rubygem-uglifier
Requires:  ruby193-rubygem-xml-simple
Requires:  ruby193-runtime

# FIXME: Need to enable these packages once they fixed in the ruby193 repo.
# Requires:  ruby193-rubygem-passenger
# Requires:  ruby193-rubygem-passenger-devel
# Requires:  ruby193-rubygem-passenger-native
# Requires:  ruby193-rubygem-passenger-native-libs
# Requires:  ruby193-mod_passenger

# FIXME: Need to enable these packages once they are in the ruby193 repo.
# Requires:  ruby193-rubygem-thread-dump
# Requires:  ruby193-rubygem-mysql
# Requires:  ruby193-rubygem-bson_ext

Requires:  mysql-devel
Requires:  ruby-devel
Requires:  libxml2
Requires:  libxml2-devel
Requires:  libxslt
Requires:  libxslt-devel
Requires:  gcc-c++
Requires:  js

%if 0%{?rhel}
Requires:  ruby-nokogiri
%endif

%if 0%{?fedora}
Requires:  rubygem-nokogiri
%endif

# Deps for users
Requires: ruby-RMagick

BuildArch: noarch

%description
Provides ruby support to OpenShift

%prep
%setup -q

%build
rm -rf git_template
cp -r template/ git_template/
cd git_template
git init
git add -f .
git config user.email "builder@example.com"
git config user.name "Template builder"
git commit -m 'Creating template'
cd ..
git clone --bare git_template git_template.git
rm -rf git_template
touch git_template.git/refs/heads/.gitignore

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{cartridgedir}
mkdir -p %{buildroot}/%{_sysconfdir}/stickshift/cartridges
ln -s %{cartridgedir}/info/configuration/ %{buildroot}/%{_sysconfdir}/stickshift/cartridges/%{name}
cp -r info %{buildroot}%{cartridgedir}/
cp LICENSE %{buildroot}%{cartridgedir}/
cp COPYRIGHT %{buildroot}%{cartridgedir}/
mkdir -p %{buildroot}%{cartridgedir}/info/data/
cp -r git_template.git %{buildroot}%{cartridgedir}/info/data/
ln -s %{cartridgedir}/../abstract/info/hooks/add-module %{buildroot}%{cartridgedir}/info/hooks/add-module
ln -s %{cartridgedir}/../abstract/info/hooks/info %{buildroot}%{cartridgedir}/info/hooks/info
ln -s %{cartridgedir}/../abstract/info/hooks/post-install %{buildroot}%{cartridgedir}/info/hooks/post-install
ln -s %{cartridgedir}/../abstract/info/hooks/post-remove %{buildroot}%{cartridgedir}/info/hooks/post-remove
ln -s %{cartridgedir}/../abstract/info/hooks/reload %{buildroot}%{cartridgedir}/info/hooks/reload
ln -s %{cartridgedir}/../abstract/info/hooks/remove-module %{buildroot}%{cartridgedir}/info/hooks/remove-module
ln -s %{cartridgedir}/../abstract/info/hooks/restart %{buildroot}%{cartridgedir}/info/hooks/restart
ln -s %{cartridgedir}/../abstract/info/hooks/start %{buildroot}%{cartridgedir}/info/hooks/start
ln -s %{cartridgedir}/../abstract-httpd/info/hooks/status %{buildroot}%{cartridgedir}/info/hooks/status
ln -s %{cartridgedir}/../abstract/info/hooks/stop %{buildroot}%{cartridgedir}/info/hooks/stop
ln -s %{cartridgedir}/../abstract/info/hooks/update-namespace %{buildroot}%{cartridgedir}/info/hooks/update-namespace
ln -s %{cartridgedir}/../abstract/info/hooks/deploy-httpd-proxy %{buildroot}%{cartridgedir}/info/hooks/deploy-httpd-proxy
ln -s %{cartridgedir}/../abstract/info/hooks/remove-httpd-proxy %{buildroot}%{cartridgedir}/info/hooks/remove-httpd-proxy
ln -s %{cartridgedir}/../abstract/info/hooks/force-stop %{buildroot}%{cartridgedir}/info/hooks/force-stop
ln -s %{cartridgedir}/../abstract/info/hooks/add-alias %{buildroot}%{cartridgedir}/info/hooks/add-alias
ln -s %{cartridgedir}/../abstract/info/hooks/tidy %{buildroot}%{cartridgedir}/info/hooks/tidy
ln -s %{cartridgedir}/../abstract/info/hooks/remove-alias %{buildroot}%{cartridgedir}/info/hooks/remove-alias
ln -s %{cartridgedir}/../abstract/info/hooks/move %{buildroot}%{cartridgedir}/info/hooks/move
ln -s %{cartridgedir}/../abstract/info/hooks/expose-port %{buildroot}%{cartridgedir}/info/hooks/expose-port
ln -s %{cartridgedir}/../abstract/info/hooks/conceal-port %{buildroot}%{cartridgedir}/info/hooks/conceal-port
ln -s %{cartridgedir}/../abstract/info/hooks/show-port %{buildroot}%{cartridgedir}/info/hooks/show-port
ln -s %{cartridgedir}/../abstract/info/hooks/system-messages %{buildroot}%{cartridgedir}/info/hooks/system-messages
mkdir -p %{buildroot}%{cartridgedir}/info/connection-hooks/
ln -s %{cartridgedir}/../abstract/info/connection-hooks/publish-gear-endpoint %{buildroot}%{cartridgedir}/info/connection-hooks/publish-gear-endpoint
ln -s %{cartridgedir}/../abstract/info/connection-hooks/publish-http-url %{buildroot}%{cartridgedir}/info/connection-hooks/publish-http-url
ln -s %{cartridgedir}/../abstract/info/connection-hooks/set-db-connection-info %{buildroot}%{cartridgedir}/info/connection-hooks/set-db-connection-info
ln -s %{cartridgedir}/../abstract/info/connection-hooks/set-nosql-db-connection-info %{buildroot}%{cartridgedir}/info/connection-hooks/set-nosql-db-connection-info
ln -s %{cartridgedir}/../abstract/info/bin/sync_gears.sh %{buildroot}%{cartridgedir}/info/bin/sync_gears.sh

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(0750,-,-) %{cartridgedir}/info/hooks/
%attr(0750,-,-) %{cartridgedir}/info/data/
%attr(0750,-,-) %{cartridgedir}/info/build/
%attr(0755,-,-) %{cartridgedir}/info/bin/
%attr(0755,-,-) %{cartridgedir}/info/connection-hooks/
%config(noreplace) %{cartridgedir}/info/configuration/
%{_sysconfdir}/stickshift/cartridges/%{name}
%{cartridgedir}/info/changelog
%{cartridgedir}/info/control
%{cartridgedir}/info/manifest.yml
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE

%changelog
* Fri Jun 15 2012 Adam Miller <admiller@redhat.com> 0.1.4-1
- Security - BZ785050 remove mod_autoindex from all httpd.confs
  (tkramer@redhat.com)

* Fri Jun 15 2012 Tim Kramer <tkramer@redhat.com>
- Security BZ785050 Removed mod_autoindex from both httpd.conf files (tkramer@redhat.com)

* Thu Jun 14 2012 Adam Miller <admiller@redhat.com> 0.1.3-1
- Use the right hook names -- thanks mpatel. (ramr@redhat.com)
- Checkpoint ruby-1.9 work (ruby-1.9 disabled for now in framework cartridges).
  Automatic commit of package [cartridge-ruby-1.9] release [0.1.1-1]. Match up
  spec file to first build version in brew and checkpoint with
  working/available ruby193 packages. (ramr@redhat.com)

* Tue Jun 12 2012 Ram Ranganathan <ramr@redhat.com>  0-1.2-1
- Automatic commit of package [cartridge-ruby-1.9] release [0.1.1-1].
  (ramr@redhat.com)
- Checkpoint ruby-1.9 work. (ramr@redhat.com)

* Tue Jun 12 2012 Ram Ranganathan <ramr@redhat.com> 0.1.1-1
- Initial version