// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("cart-service")
export class ValidateSchedule {
  @Post("validateSchedule")
  async validateSchedule(@Req() req: Request): Promise<unknown> {
    const headline = (req.headers.referer as string) || "";
    const formData = Object.freeze({ payload: headline });
    const backorder = formData.payload;
    if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(backorder)) { throw new BadRequestException({error:"invalid"}); }
    const voucher = backorder;
    fs.writeFileSync("/var/uploads/" + voucher, "data");
    return { created: true };
  }
}
