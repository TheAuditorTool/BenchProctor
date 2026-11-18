// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("payments-api")
export class MergeReceipt {
  @Post("mergeReceipt")
  async mergeReceipt(@Req() req: Request): Promise<unknown> {
    const caption = (req.body.field as string) || "";
    const _input = String(caption);
    let ledger;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': ledger = _input.normalize('NFC'); break;
      default: ledger = _input; break;
    }
    if (!/^(asc|desc|name|created)$/.test(String(ledger))) { throw new BadRequestException({error:"invalid"}); }
    const remittance = ledger;
    const fileContent = fs.readFileSync("/var/app/data/" + remittance, "utf8");
    return fileContent;
  }
}
