# Squad Maker Comments

The project is now complete to the requirements and my general standards for what I would put up for review with the team, expecting only minor issues to discuss before putting it up for acceptance with the stakeholders.

I made some assumptions about the target level of quality, based on the language used to describe the target customer and target audience. This includes assumptions about the need to serve only one organizer for only one tournament at a time. That plus the recreational nature of the tournament implied that a 'functional' approach to the requirements would be sufficient.

None the less, here is a listing of topics that came up during development (or would come up with a different target customer/market) that were excluded from the solution presented.

# DevOps Topics
* Continuous Integration/Continuous Deployment (CI/CD)
** WIth one developer, going much beyond a Makefile was going to be overkill here. If the project was expected to be any larger and support concurrent sustained development it would be important to set up a CI pipeline. A CD pipeline might be nice to have, but it would depend on the customers interest/tolerance.
* Containerized deployment
** Would help a lot with CD, but with a single actual deployment this is left as a future optimization. If it required even one more node or one more deployment, I'd do this first.
* Deployment configs in source control
** With only one temporary VM to demo the project on, there isn't really anything to commit here. However, if I was maintaining the running service I would make a second repo to keep the operation configs in. A simple bit of Ansible would be sufficient for a project of this type.


# Quality/Maintainability Topics
* Documentation
** The project is sufficiently described in docstrings where necessary for me to feel confident handing this off to another engineer I have raport with, such as Travis or Glen. The project is not sufficiently documented to hand off to a non-technical person, or an operations-specific engineer that I have no raport with.
** Auto-docs would be the way to go here, building documentation automation that extends and compiles together the source code documentation with non-technical prose that could be served off the same webserver as the project itself.
* Automated targets for style checking
** Nice to have for longer term development and keeping things consistent. Save time on arguing about style by automating it upfront! I used yapf to auto-format all the python code, so it would be easy to include that in the requirements and make targets.
* Automated targets for lint checking
** Similarly nice to have for development, providing some framework for it in the repo as a courtesy instead of leaving it for people to configure their editor to do or what have you. Particularly useful as a sanity check for a CI pipeline.
* Automated testing for webservice
** I'm unaware as to the best practices for how to automate testing of a webservice without it turning into a rather large effort of automated deployments etc. Since I wasn't doing automated deployment I omitted this bit, but felt dirty in doing so.

# Further Requirements Topics
* Concurrency/Multi-tenancy
** The current model only has one view of the world, so two users could get confusing behaviour out of the system.
* Fault tolerance
** Resistance to malicious input. I only did basic sanity testing on data ranges, but for the html form stuff there could be more sanitization and error guarding.
** High availability deployment. Only one node so if a problem comes up, the tournament will be unable to start! Hopefully Digital Ocean doesn't have an outtage when the customer needs his hockey teams generated.