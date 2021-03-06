import { Injectable } from '@angular/core';

@Injectable()
export class ModelService {

    private selectedDelays : Delay[] = []

    constructor() { }

    addSelectedDelay(delay : Delay) {
        this.selectedDelays.push(delay)
    }

    removeSelectedDelay(delay : Delay) {
        for(let i = 0; i < this.selectedDelays.length; i++) {
            let currentDelay : Delay = this.selectedDelays[i]
            if(currentDelay.id == delay.id) {
                this.selectedDelays.splice(i, 1)
                i--
            }
        }
    }

    isSelected(delayId : number) : boolean {
        return this.selectedDelays.find((value) => +value.id == delayId)? true : false
    }

    removeSelectedDelayById(delayId : number) {
        this.selectedDelays.splice(this.selectedDelays.findIndex((value) => +value.id == delayId), 1) 
    }

    setSelectedDelays(selectedDelays : Delay[]) {
        this.selectedDelays = selectedDelays
    }

    getSelectedDelays() : Delay[] {
        return this.selectedDelays
    }
}