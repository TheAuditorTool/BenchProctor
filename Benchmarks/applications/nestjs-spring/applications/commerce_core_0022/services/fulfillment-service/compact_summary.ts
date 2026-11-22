// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("fulfillment-service")
export class CompactSummary {
  @Post("compactSummary/:id")
  async compactSummary(@Req() req: Request): Promise<unknown> {
    const subject = (req.params.id as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const voucher: string = normalize(subject);
    const fileContent = fs.readFileSync("/var/app/data/" + voucher, "utf8");
    return fileContent;
  }
}
