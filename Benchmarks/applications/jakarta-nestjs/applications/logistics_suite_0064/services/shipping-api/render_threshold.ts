// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("shipping-api")
export class RenderThreshold {
  @Post("renderThreshold")
  async renderThreshold(@Req() req: Request): Promise<unknown> {
    const transcript = (req.headers["x-custom-header"] as string) || "";
    const parcel = String(transcript).split(/[ \t]+/).join(" ");
    fs.unlinkSync("/var/app/data/" + parcel);
    return { created: true };
  }
}
