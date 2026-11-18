// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("billing-api")
export class NormalizeIndex {
  @Post("normalizeIndex")
  async normalizeIndex(@Req() req: Request): Promise<unknown> {
    const remark = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(remark).split(',')) { parts.push(token); }
    const remittance: string = parts.join(',');
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(remittance)) { throw new BadRequestException({error:"invalid"}); }
    const arrears = remittance;
    return "<div>" + arrears + "</div>";
  }
}
