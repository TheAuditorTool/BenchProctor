// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("reservation-service")
export class HoldReservation {
  @Post("holdReservation")
  async holdReservation(@Req() req: Request): Promise<unknown> {
    const transcript = (req.body.payload as string) || "";
    const transform = (v: string): string => v.trim();
    const backorder: string = transform(transcript);
    await fetch("http://catalog-api:8080/LookupSku", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({inventory_payload: backorder})});
    return { created: true };
  }
}
