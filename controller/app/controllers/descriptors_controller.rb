class DescriptorsController < BaseController
  respond_to :xml, :json
  before_filter :authenticate, :check_version
  
  def show
    domain_id = params[:domain_id]
    application_id = params[:application_id]
    
    domain = Domain.get(@cloud_user, domain_id)
    return render_error(:not_found, "Domain #{domain_id} not found", 127,
                        "SHOW_DESCRIPTOR") if !domain || !domain.hasAccess?(@cloud_user)

    @domain_name = domain.namespace
    application = Application.find(@cloud_user,application_id)
    return render_error(:not_found, "Application '#{application_id}' not found for domain '#{domain_id}'",
                        101, "SHOW_DESCRIPTOR") unless application
    
    @application_name = application.name
    @application_uuid = application.uuid
    render_success(:ok, "descriptor", application.to_descriptor.to_yaml, "SHOW_DESCRIPTOR",
                   "Show descriptor for application '#{application_id}' for domain '#{domain_id}'")
  end
end
