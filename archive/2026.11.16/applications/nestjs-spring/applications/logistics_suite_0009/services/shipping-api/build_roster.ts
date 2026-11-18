// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("shipping-api")
export class BuildRoster {
  @Post("buildRoster")
  async buildRoster(@Req() req: Request): Promise<unknown> {
    const subject = (req.headers.authorization as string) || "";
    const parcel = Buffer.from(subject, "base64").toString();
    return "<div>" + parcel + "</div>";
  }
}
