// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("cart-service")
export class FormatManifest {
  @Post("formatManifest")
  async formatManifest(@Req() req: Request): Promise<unknown> {
    const memo = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(memo).split(',')) { parts.push(token); }
    const voucher: string = parts.join(',');
    fs.unlinkSync("/var/app/data/" + voucher);
    return { created: true };
  }
}
