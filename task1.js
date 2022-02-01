/// <reference types = "Cypress"/>

describe('Task 1: Test contact us for not logged in user', ()=>{


    it('Fill out the form & send message', ()=>{

        //visite the site
        cy.visit('http://automationpractice.com/index.php')
        cy.contains('Contact us').click()
        cy.url().should('include', 'controller=contact')

        //select Customer service
        cy.get('.selector').click().should('be.visible').contains("Customer service")
        cy.get('select').select('Customer service')
        
        //fill out input fields
        cy.get('.form-control.grey.validate').type('fake@email.com').should('have.value', 'fake@email.com')
        cy.get('input[id = id_order]').type('test').should('have.value','test')
        cy.get('textarea[id = message]'). type ('hei').should('have.value', 'hei')

        //send message
        cy.contains('Send').click()
        cy.get('.alert.alert-success').contains('Your message has been successfully sent to our team.')
    })

})

