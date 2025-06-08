# Django-DocumentManagement2
 phase2 of document management (March 16-30)

The principal is member of the commitee so he/she has two accounts
	
	user: com1 (the uploader) -> School Head
	pass: demo1234

	user: principal (the approver)
	pass: demo1234

The Members of the Commitee will have only one account (uploaders)

	user:	pass:
	com2	demo1234 -> Leadership
	com3	demo1234 -> Internal Stakeholders
	com4	demo1234 -> External Stakeholders
	com5	demo1234 -> School Improvement Resources
	com6	demo1234 -> School-Based Resources
	com7	demo1234 -> School Performance Accountability

This users can change their own password in the dashboard(upperright corner).
This type of scheme is created base sa diagrams.

a. Phase 1 &#9745;
b. Phase 2 &#9745;

c. SKIPPED
8̶,̶0̶0̶0̶ ̶p̶h̶p̶ ̶(̶o̶p̶t̶i̶o̶n̶a̶l̶ ̶a̶d̶d̶o̶n̶s̶)̶(̶p̶a̶y̶ ̶t̶o̶ ̶a̶d̶d̶)̶
	^̶1. C̶r̶e̶a̶t̶e̶ ̶w̶e̶b̶a̶p̶p̶ ̶a̶d̶m̶i̶n̶-̶i̶n̶t̶e̶r̶f̶a̶c̶e̶-̶c̶u̶s̶t̶o̶m̶ ̶t̶e̶m̶p̶l̶a̶t̶e̶ ̶f̶o̶r̶ ̶c̶u̶s̶t̶o̶m̶i̶z̶a̶t̶i̶o̶n̶ ̶o̶f̶ ̶i̶t̶s̶ ̶u̶i̶,̶ ̶r̶a̶t̶h̶e̶r̶ ̶t̶h̶a̶n̶ ̶c̶o̶d̶e̶-̶i̶t̶ m̶a̶n̶u̶a̶l̶l̶y̶ ̶(̶w̶o̶r̶d̶p̶r̶e̶s̶s̶ ̶c̶m̶s̶ ̶a̶l̶i̶k̶e̶)̶ 
	̶^̶2. C̶r̶e̶a̶t̶e̶ ̶a̶ ̶d̶o̶c̶u̶m̶e̶n̶t̶_̶l̶i̶s̶t̶_̶p̶a̶g̶e̶'̶s̶ ̶i̶m̶p̶o̶r̶t̶/̶e̶x̶p̶o̶r̶t̶ ̶p̶l̶u̶g̶i̶n̶ ̶i̶n̶ ̶j̶s̶o̶n̶ ̶o̶r̶ ̶c̶s̶v̶ ̶f̶o̶r̶m̶a̶t̶(̶f̶o̶r̶ ̶d̶a̶t̶a̶ ̶f̶i̶e̶l̶d̶ b̶a̶c̶k̶u̶p̶s̶)̶.̶
	̶^̶3. C̶r̶e̶a̶t̶e̶ ̶a̶ ̶d̶o̶c̶u̶m̶e̶n̶t̶_̶l̶i̶s̶t̶_̶p̶a̶g̶e̶'̶s̶ ̶a̶p̶p̶r̶o̶v̶e̶d̶_̶f̶i̶l̶e̶s̶_̶d̶o̶w̶n̶l̶o̶a̶d̶e̶r̶ ̶p̶l̶u̶g̶i̶n̶ ̶i̶f̶ ̶a̶d̶m̶i̶n̶ ̶w̶a̶n̶t̶s̶ ̶t̶o̶ ̶d̶o̶w̶n̶l̶o̶a̶d̶ t̶h̶e̶ ̶a̶p̶p̶r̶o̶v̶e̶d̶ ̶m̶e̶d̶i̶a̶ ̶d̶o̶c̶u̶m̶e̶n̶t̶s̶.̶
	̶^̶4. C̶r̶e̶a̶t̶e̶ ̶a̶ ̶d̶o̶c̶u̶m̶e̶n̶t̶_̶l̶i̶s̶t̶_̶p̶a̶g̶e̶'̶s̶ ̶m̶u̶l̶t̶i̶p̶l̶e̶ ̶a̶p̶p̶r̶o̶v̶e̶d̶/̶d̶i̶s̶a̶a̶p̶r̶o̶v̶e̶d̶ ̶p̶l̶u̶g̶i̶n̶ ̶f̶o̶r̶ ̶m̶a̶s̶s̶ ̶c̶h̶a̶n̶g̶e̶,̶i̶n̶s̶t̶e̶a̶d̶ o̶f̶ ̶o̶n̶e̶-̶b̶y̶-̶o̶n̶e̶ ̶n̶e̶w̶t̶a̶b̶ ̶a̶p̶p̶r̶o̶v̶e̶
	̶^̶5. C̶r̶e̶a̶t̶e̶ ̶a̶ ̶d̶o̶c̶u̶m̶e̶n̶t̶_̶l̶i̶s̶t̶_̶p̶a̶g̶e̶'̶s̶ ̶s̶e̶a̶r̶c̶h̶_̶f̶i̶e̶l̶d̶ ̶p̶l̶u̶g̶i̶n̶ ̶w̶h̶e̶r̶e̶ ̶a̶d̶m̶i̶n̶/̶p̶r̶i̶n̶c̶i̶p̶a̶l̶ ̶c̶a̶n̶ ̶s̶e̶a̶r̶c̶h̶ u̶s̶e̶r̶n̶a̶m̶e̶,̶t̶i̶t̶l̶e̶_̶o̶f̶_̶d̶o̶c̶u̶m̶e̶n̶t̶,̶u̶p̶l̶o̶a̶d̶e̶d̶_̶d̶a̶t̶e̶.̶
	̶^̶6. C̶r̶e̶a̶t̶e̶ ̶a̶ ̶d̶o̶c̶u̶m̶e̶n̶t̶_̶l̶i̶s̶t̶_̶p̶a̶g̶e̶'̶s̶ ̶f̶i̶l̶t̶e̶r̶_̶b̶y̶_̶t̶y̶p̶e̶ ̶b̶e̶s̶i̶d̶e̶s̶ ̶t̶h̶e̶ ̶a̶p̶p̶r̶o̶v̶e̶d̶_̶d̶i̶s̶a̶p̶p̶r̶o̶v̶e̶_̶p̶e̶n̶d̶i̶n̶g̶ ̶f̶i̶l̶t̶e̶r̶.̶
	̶^̶7. C̶r̶e̶a̶t̶e̶ ̶a̶ ̶d̶j̶a̶n̶g̶o̶-̶f̶a̶k̶e̶ ̶l̶o̶g̶i̶n̶ ̶f̶o̶r̶ ̶s̶e̶c̶u̶r̶i̶t̶y̶ ̶p̶u̶r̶p̶o̶s̶e̶s̶
	̶^̶8. C̶r̶e̶a̶t̶e̶ ̶a̶ ̶n̶e̶w̶ ̶r̶o̶l̶e̶ ̶n̶a̶m̶e̶d̶ ̶s̶u̶p̶e̶r̶a̶d̶m̶i̶n̶ ̶w̶h̶e̶r̶e̶ ̶i̶t̶ ̶h̶a̶s̶ ̶a̶c̶c̶e̶s̶s̶ ̶t̶o̶ ̶a̶l̶l̶ ̶d̶a̶t̶a̶ ̶a̶n̶d̶ ̶c̶a̶n̶ a̶d̶d̶.̶d̶e̶l̶e̶t̶e̶.̶u̶p̶d̶a̶t̶e̶ ̶u̶s̶e̶r̶ ̶i̶n̶f̶o̶r̶m̶a̶t̶i̶o̶n̶s̶.̶

d. SKIPPED
2̶,̶0̶0̶0̶ ̶p̶h̶p̶ ̶(̶o̶p̶t̶i̶o̶n̶a̶l̶ ̶a̶d̶d̶o̶n̶s̶)̶(̶p̶a̶y̶ ̶t̶o̶ ̶a̶d̶d̶)̶ ̶>̶ ̶
	̶ ̶^̶1. A̶d̶d̶ ̶n̶a̶m̶e̶s̶e̶r̶v̶e̶r̶s̶,̶ ̶c̶o̶n̶f̶i̶g̶ ̶d̶n̶s̶ ̶f̶o̶r̶ ̶r̶e̶a̶d̶a̶b̶l̶e̶ ̶a̶d̶d̶r̶e̶s̶s̶ ̶i̶n̶s̶t̶e̶a̶d̶ ̶o̶f̶ ̶u̶s̶i̶n̶g̶ ̶1̶2̶7̶.̶0̶.̶0̶.̶1̶/̶l̶o̶c̶a̶l̶h̶o̶s̶t̶ ̶y̶o̶u̶ ̶c̶a̶n̶
	̶ ̶j̶u̶s̶t̶ ̶t̶y̶p̶e̶ ̶y̶o̶u̶r̶a̶p̶p̶.̶e̶x̶a̶m̶p̶l̶e̶.̶c̶o̶m̶
	̶ ̶2. D̶e̶p̶l̶o̶y̶ ̶i̶t̶ ̶o̶n̶ ̶v̶p̶s̶,̶h̶o̶s̶t̶i̶n̶g̶ ̶w̶e̶b̶s̶i̶t̶e̶s̶,̶ ̶o̶r̶ ̶a̶ ̶l̶o̶c̶a̶l̶ ̶s̶e̶r̶v̶e̶r̶ ̶l̶i̶k̶e̶ ̶p̶c̶ ̶o̶r̶ ̶r̶a̶s̶p̶b̶e̶r̶r̶y̶ ̶p̶i̶s̶,̶ ̶o̶r̶ ̶a̶n̶y̶ ̶n̶e̶t̶w̶o̶r̶k̶ ̶t̶h̶a̶t̶
	̶ ̶h̶a̶s̶ ̶a̶n̶ ̶a̶c̶c̶e̶s̶s̶ ̶p̶o̶i̶n̶t̶.̶

Accomplishments as of May. Upon downloading the repository and liking this message means
the user agreed to how the project is upgraded and all changes and added functionality 
are base on the Client's Own Messenger-Chats dated May 27-28 2025.

NOTE THIS IS CONSIDERED AS A NEW CONTRACT 
Php 8,000 (addons)(paytoadd)(charge-rate is still base on the old finished project contract)
(The development will begin once the payment is received) ~ 1-2 weeks
	
	(No need for long explanation, Ill just place the keywords instead)
	1. rebranding the project-name &#9745;
	2. renaming a link per page &#9745;
	3. adding back/redirect button on change/add_form &#9745;
	4. adding the logo and fav.ico(logo on the tab-browser & its webfrontend) &#9745;
	5. adding print functions for image and pdf on document-list & view_form &#9745;
	6. adding necessary js-scripts and adjustment of some huge blocks of code (hard-coding). &#9745;
	7. testing some of the added codes if it breaks/conflicts the existing project. &#9745;

Upon the successful completion of the above items, the upgrade of the web application will be 
considered finalized and delivered, and no additional features, revisions, or enhancements will 
be made. Future changes will require a new contract and development plan.