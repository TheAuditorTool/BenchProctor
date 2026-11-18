// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("order-history")
export class CompactRoster {
  @Post("compactRoster")
  async compactRoster(@Req() req: Request): Promise<unknown> {
    const heading = (req.body.field as string) || "";
    const _input = String(heading);
    let voucher;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': voucher = _input.normalize('NFC'); break;
      default: voucher = _input; break;
    }
    if (!/^(asc|desc|name|created)$/.test(String(voucher))) { throw new BadRequestException({error:"invalid"}); }
    const backorder = voucher;
    const fileContent = fs.readFileSync("/var/app/data/" + backorder, "utf8");
    return fileContent;
  }
}
