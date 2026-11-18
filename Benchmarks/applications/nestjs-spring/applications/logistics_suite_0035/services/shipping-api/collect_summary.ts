// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("shipping-api")
export class CollectSummary {
  @Post("collectSummary")
  async collectSummary(@Req() req: Request): Promise<unknown> {
    const phrase = (req.headers.host as string) || "";
    const parcel = `${phrase}`;
    http.get(parcel);
    return { created: true };
  }
}
