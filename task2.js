/// <reference types = "Cypress"/>

describe("Task 2", ()=>{
    beforeEach(()=>{
        //visit the site
        cy.visit('http://automationpractice.com/index.php')
        .contains('Sign in').click()
        .url().should('include', 'controller=authentication&back=my-account')

        //login
        cy.get('input[id = email]').type('fakeadress@email.com').should('have.value', 'fakeadress@email.com')
        .get('input[id = passwd]').type('12345').should('have.value','12345')
        .get('#SubmitLogin').click()
        .url().should('include','controller=my-account')
    })
    
    describe('Purchase an item', ()=>{

        it('Place an order as logged in user', ()=>{
           
            //Add item to cart
            cy.visit('http://automationpractice.com/index.php')
            .get('.button-container')
            .get('[data-id-product=1]').contains('Add to cart').click()
            
            //Go to checkout
            cy.contains('Proceed to checkout').click()
            .url().should('include', 'controller=order')
    
            //Show shopping cart & go to address confirmation
            cy.get('a[href*="controller=order&step=1"]').click()
            .url().should('include','controller=order&step=1')

            //Show adress & got to shipping
            cy.get('[name=processAddress]').click()
            .url().should('include','controller=order')

            //Agree to terms & go to payment
            cy.get('[type = checkbox]').check()
            .should('be.checked')
            .get('[name=processCarrier]').click()
    
            //choose payment & go to order confirmation
            cy.get('a[href*="fc=module&module=cheque&controller=payment"]').click()
            .url().should('include','controller=payment')
            
            //Confirm order
            cy.get('.btn').contains('I confirm my order').click()
            .url().should('include', 'controller=order-confirmation')
            .get('.alert.alert-success').contains('Your order on My Store is complete.')
    
    
        })
    })
    describe('Send to friend', () => {

        it('can send an item to a friend', ()=>{

            //visit the site
            cy.visit('http://automationpractice.com/index.php')

            //choose a product
            cy.contains('More').click()
            cy.url().should('include', 'product')

            //click on "send to friend"
            cy.contains('Send to a friend').click()

            //fill out the form
            cy.get('#friend_name')
            .type('Test Friend')
            .should('have.value', 'Test Friend')
                
            cy.get('#friend_email')
            .type('test@mail.com')
            .should('have.value', 'test@mail.com')     

            //send
            cy.get('[name=sendEmail]').click()

            cy.go('back')

        })
    
    })

    describe('Add item to wishlist:',function(){

        it('adds item to wishlist, after login', ()=>{
            //finner et plagg a legge til i favoritter
          cy.get('.sf-menu > :nth-child(1) > [href="http://automationpractice.com/index.php?id_category=3&controller=category"]').click()
          cy.get(':nth-child(1) > .subcategory-image > .img > .replace-2x').click()
      
          //legger til i favoritter
          cy.get('.first-in-line > .product-container > .functional-buttons > .wishlist > .addToWishlist').click()
          cy.get('.fancybox-error').should('be.visible')
          cy.get('.fancybox-item').click()
      
          //tilbake til accounten
          cy.get('.account').click()
          cy.url().should('include', 'controller=my-account')
      
          //finne favorittlisten
          cy.get('.lnk_wishlist > a > span').click()
      
          //sjekker om den er synlig
          cy.get('#block-history').contains('My wishlist').click()
          cy.get('.wlp_bought_list').should('be.visible')
      
        })
      
          
         
    })
    

    afterEach(()=>{
        //logout
        cy.contains('Sign out').click()
    })
})