// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("checkout-gateway")
export class FetchPromotion {
  @Post("fetchPromotion")
  async fetchPromotion(@Req() req: Request): Promise<unknown> {
    const wording = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(wording).split(',')) { parts.push(token); }
    const backorder: string = parts.join(',');
    if (!/^(asc|desc|name|created)$/.test(String(backorder))) { throw new BadRequestException({error:"invalid"}); }
    const voucher = backorder;
    fs.unlinkSync("/var/app/data/" + voucher);
    return { created: true };
  }
}
