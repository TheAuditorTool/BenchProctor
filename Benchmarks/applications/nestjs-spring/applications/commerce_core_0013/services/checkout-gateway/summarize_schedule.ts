// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("checkout-gateway")
export class SummarizeSchedule {
  @Post("summarizeSchedule")
  async summarizeSchedule(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers.host as string) || "";
    const backorder = wording != null ? wording : '';
    if (!/^(asc|desc|name|created)$/.test(String(backorder))) { throw new BadRequestException({error:"invalid"}); }
    const voucher = backorder;
    fs.writeFileSync("/var/uploads/" + voucher, "data");
    return { created: true };
  }
}
