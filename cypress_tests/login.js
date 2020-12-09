context('Startup', () => {
  beforeEach(() => {
    cy.visit('https://hedonisticopportunist.github.io/framework_tests/site/login.html');
  });
  
   it('Should fill out the login form and redirect to the dashboard', () => {
	   
	   cy.title().should('eq', 'Login 💀')
	   cy.get('form')
	   cy.get('input[name="username"]')
	   .type('user')
	   
	   cy.get('input[name="password"]')
	   .type('holden')
	   
	   cy.get('[name="submit"]').click();
	   
	   cy.title()
	   .should('eq', 'Dashboard 💀')
	   
	   cy.get('h1')
	   .contains('Muppet Musical :P')
	   
	   cy.location()
	   .should((loc) => {
		   expect(loc.pathname.toString()).to.contain('/dashboard');
		   
 });
   
  });
  
});
