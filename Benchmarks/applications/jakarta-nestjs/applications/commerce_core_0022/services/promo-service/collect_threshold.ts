// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("promo-service")
export class CollectThreshold {
  @Post("collectThreshold")
  async collectThreshold(@Req() req: Request): Promise<unknown> {
    const subject = (req.headers.referer as string) || "";
    const formData = Object.freeze({ payload: subject });
    const voucher = formData.payload;
    if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(voucher)) { throw new BadRequestException({error:"invalid"}); }
    const backorder = voucher;
    fs.writeFileSync("/var/uploads/" + backorder, "data");
    return { created: true };
  }
}
