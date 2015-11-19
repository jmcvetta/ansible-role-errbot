require 'serverspec'
set :backend, :exec

describe service('errbot') do
	it { should be_enabled }
	it { should be_running }
end
