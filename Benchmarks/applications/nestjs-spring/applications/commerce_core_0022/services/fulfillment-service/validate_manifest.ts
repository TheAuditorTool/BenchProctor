// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("fulfillment-service")
export class ValidateManifest {
  @Post("validateManifest")
  async validateManifest(@Req() req: Request): Promise<unknown> {
    const subject = (req.body?.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(subject).split(',')) { parts.push(token); }
    const voucher: string = parts.join(',');
    if (!/^(asc|desc|name|created)$/.test(String(voucher))) { throw new BadRequestException({error:"invalid"}); }
    const backorder = voucher;
    fs.unlinkSync("/var/app/data/" + backorder);
    return { created: true };
  }
}
