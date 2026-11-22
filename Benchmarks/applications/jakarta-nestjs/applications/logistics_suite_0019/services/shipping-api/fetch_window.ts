// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("shipping-api")
export class FetchWindow {
  @Post("fetchWindow")
  async fetchWindow(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers.host as string) || "";
    const [parcel] = String(citation).split(',');
    http.get(parcel);
    return { created: true };
  }
}
