context('Startup', () => {
  beforeEach(() => {
    cy.visit('https://hedonisticopportunist.github.io/framework_tests/login.html');
  });
  
   it('Should fill out the login form and redirect to the dashboard', () => {
	   
	   cy.get('form')
	   cy.get('input[name="username"]')
	   .type('user')
	   .should('have.value', 'user');
	   
	   cy.get('input[name="password"]')
	   .type('holden')
	   .should('have.value', 'holden');
	   
	   cy.get('[name="submit"]').click();
	   
	   cy.location().should((loc) => {
		   expect(loc.pathname.toString()).to.contain('/dashboard');
 });
   
  });
  
});
