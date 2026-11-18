// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("customs-service")
export class FetchConfig {
  @Post("fetchConfig")
  async fetchConfig(@Req() req: Request): Promise<unknown> {
    const caption = (req.query.id as string) || "";
    const [parcel] = String(caption).split(',');
    return "<div>" + parcel + "</div>";
  }
}
