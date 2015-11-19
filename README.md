errbot
======

Ansible role to deploy [Errbot](http://errbot.io/), a Python-based
[ChatOps](https://www.pagerduty.com/blog/what-is-chatops/) bot.

Requirements
------------

This role is tested against the platforms show below.  Other Linux flavors may
work but are not supported - YMMV.

```yaml
platforms:
  - name: ubuntu-14.04
  - name: centos-7.1
```

Testing
-------

This role can be tested using [Test Kitchen](http://kitchen.ci).  

```bash
bundle install
kitchen test
```


Role Variables
--------------

n/a


Dependencies
------------

n/a

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: errbot_servers
      roles:
         - role: jason.mcvetta.errbot


License
-------

Apache v2


Author Information
------------------

Jason McVetta <jason.mcvetta@gmail.com>
