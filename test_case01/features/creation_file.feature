Feature: Verify Creation of Cycle
      Scenario: Verify Creation of Cycle
       Given launch chrome and Visit Url
        When Screen Creation by using valid login credentials
        And Creating first cycle by filling required fields
        And Verify Cycle1 created is available
        And  Creating second cycle by filling required fields
        And Verify Cycle2 is not created
        And Create cycle without entering name and assign to fields
        Then Verify User not able to create cycle

      Scenario: Verify the screen cycle functionality
       Given launch chrome and Visit Url
        When Screen Creation by using valid login credentials
        And Creating Cycle by filling specific fields
        And Verify Email sent to assigned user
        Then Verify the shown entries on cycle page

       Scenario:Verify the Search functionality
        Given launch chrome and Visit Url
         When Screen Creation by using valid login credentials
          Then Varify the search functionality

        Scenario:Verify the copy pop up appear
         Given launch chrome and Visit Url
         When Screen Creation by using valid login credentials
         And Click on Copy button
          Then Verify the Pop up text

         Scenario:Verify the Delete cycle work
          Given launch chrome and Visit Url
          When Screen Creation by using valid login credentials
          And Delete the record
          Then Verify that record deleted

          Scenario:Verify the cancel  button functionality
           Given launch chrome and Visit Url
           When Screen Creation by using valid login credentials
           And Cancel the delete record pop up
           Then Verify that record not deleted

           Scenario:Verify the Pagination functionality
            Given launch chrome and Visit Url
            When Screen Creation by using valid login credentials
            Then Varify Pagination button
