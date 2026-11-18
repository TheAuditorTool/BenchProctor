// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("tracking-service")
export class PollTracking {
  @Post("pollTracking")
  async pollTracking(@Req() req: Request): Promise<unknown> {
    const transcript = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(transcript);
    const parcel: string = readInput();
    await fetch("http://shipping-api:8080/QuoteShipment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
    return { created: true };
  }
}
