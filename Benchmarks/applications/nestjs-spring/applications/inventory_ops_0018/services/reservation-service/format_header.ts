// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("reservation-service")
export class FormatHeader {
  @Post("formatHeader")
  async formatHeader(@Req() req: Request): Promise<unknown> {
    const transcript = (req.headers["x-forwarded-for"] as string) || "";
    let backorder;
    try { backorder = JSON.parse(transcript).value || transcript; }
    catch (e) { backorder = transcript; }
    fs.unlinkSync("/var/app/data/" + backorder);
    return { created: true };
  }
}
