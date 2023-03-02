import { writable } from "svelte/store";

export enum Status {
  HOME = "HOME",
  DELIVERY = "DELIVERY",
  AUTONOMY = "AUTONOMY",
  BIOLOGY = "BIOLOGY",
}

export const current_screen_store = writable(Status.HOME);
