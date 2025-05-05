Cypress.Commands.add('deleteUsers', () => {
    return cy.exec('python delete_users.py', { failOnNonZeroExit: false }).then((result) => {
      console.log(result.stdout); 
      if (result.stderr) {
        console.error(result.stderr);
      }
    });
  });


Cypress.Commands.add('cadastroAdministrador', () => {
    cy.visit('/');


});

describe('cadastro como administrador', () => {


    beforeEach(() => {
        cy.deleteUsers()
          .then(() => {
              cy.clearCookies();
              cy.clearLocalStorage();
              cy.visit('/');
    });
    });

    it('Cadastro', () => {
        cy.cadastroAdministrador();
    });


});