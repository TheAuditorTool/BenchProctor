// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("payout-service")
export class EnrichDigest {
  @Post("enrichDigest")
  async enrichDigest(@Req() req: Request): Promise<unknown> {
    const headline = (req.cookies?.session_token as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const disbursement: string = normalize(headline);
    if (!/^(asc|desc|name|created)$/.test(String(disbursement))) { throw new BadRequestException({error:"invalid"}); }
    const remittance = disbursement;
    fs.unlinkSync("/var/app/data/" + remittance);
    return { created: true };
  }
}
