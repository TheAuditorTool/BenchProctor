// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("payout-service")
export class EnrichConfig {
  @Post("enrichConfig")
  async enrichConfig(@Req() req: Request): Promise<unknown> {
    const headline = (req.headers["x-forwarded-for"] as string) || "";
    const disbursement = headline != null ? headline : '';
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(disbursement)) { throw new BadRequestException({error:"invalid"}); }
    const remittance = disbursement;
    return "<div>" + remittance + "</div>";
  }
}
