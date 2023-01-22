import { writable } from 'svelte/store';

export enum HomeScreen {
    DEFAULT,
    SERVICE,
    DELIVERY,
    AUTONOMOUS,
    BIOLOGY,
    TEST,
    SETTINGS
}

export const current_screen_store = writable(HomeScreen.DEFAULT);