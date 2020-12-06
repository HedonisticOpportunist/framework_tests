context('Startup', () => {
  beforeEach(() => {
    cy.visit('https://hedonisticopportunist.github.io/framework_tests/login.html');
  });
  
   it('Should not redirect to the dashboard', () => {
	   
	   cy.title().should('eq', 'Login 💀')
	   cy.get('form')
	   cy.get('input[name="username"]')
	   .type('rsa')
	   
	   cy.get('input[name="password"]')
	   .type('rsa')
	   
	   cy.get('[name="submit"]').click();
	   
	   cy.title().should('eq', 'Login 💀')
	   cy.get('h1')
	   .contains('Login')
		   
 });
});