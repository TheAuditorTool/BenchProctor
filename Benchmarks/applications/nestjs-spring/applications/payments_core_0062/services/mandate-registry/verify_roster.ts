// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("mandate-registry")
export class VerifyRoster {
  @Post("verifyRoster")
  async verifyRoster(@Req() req: Request): Promise<unknown> {
    const headline = (req.body?.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(headline).split(',')) { parts.push(token); }
    const disbursement: string = parts.join(',');
    if (!/^(asc|desc|name|created)$/.test(String(disbursement))) { throw new BadRequestException({error:"invalid"}); }
    const remittance = disbursement;
    fs.unlinkSync("/var/app/data/" + remittance);
    return { created: true };
  }
}
