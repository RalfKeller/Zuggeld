import { Component, OnInit } from '@angular/core';
import { CommService } from '../Services/comm.service';
import { ModelService } from '../Services/model.service';

@Component({
    selector: 'listComp',
    templateUrl: 'list.component.html'
})

export class ListComponent implements OnInit {
    
    private allDelays : Delay[]
    private filteredDelays : Delay[]
    private selectedDelays : Delay[]
    private shownDelays : Delay[]

    private delaysPerPage : number = 6

    private pages : number  = 1
    private pagesArr : number[] = [1]
    private currentPage : number = 1

    private searchString : string = ""
    
    constructor(private commService : CommService, private modelService : ModelService) { }

    ngOnInit() { 
        this.commService.getDelays().subscribe((delays) => {
            this.allDelays = delays
            this.filteredDelays = delays
            this.shownDelays = delays.slice(0, this.delaysPerPage)
            this.selectedDelays = []
            this.refreshPagination()
        })
    }

    refreshPagination() {
        this.pages = Math.ceil(this.filteredDelays.length / this.delaysPerPage)
        this.pagesArr = []

        for(let i = 1; i <= this.pages; i++) {
            this.pagesArr.push(i)
        }
    }

    goToPage(newPage : number) {
        this.currentPage = newPage
        this.shownDelays = this.filteredDelays.slice((newPage - 1) * this.delaysPerPage, (newPage) * this.delaysPerPage)
    }

    onSearchChanged() {
        console.log(this.searchString)
        this.filteredDelays = []
        for(let delay of this.allDelays) {

            if((delay.von.indexOf(this.searchString) != -1) || (delay.nach.indexOf(this.searchString) != -1) || (delay.datum.indexOf(this.searchString) != -1)) {
                this.filteredDelays.push(delay)
            }
        }

        this.goToPage(1)
        this.refreshPagination()
    }

    pageUp() {
        if(this.currentPage < this.pages) {
            this.goToPage(this.currentPage + 1)
        }
    }

    pageDown() {
        if(this.currentPage > 1) {
            this.goToPage(this.currentPage - 1)
        }
    }

    onCheckboxChanged(event, delayId : number) {
        if(event.srcElement.checked) {
            this.modelService.addSelectedDelay(this.allDelays.find((value) => +value.id == delayId))
        }
        else {
            this.modelService.removeSelectedDelayById(delayId)
        }
     }
}