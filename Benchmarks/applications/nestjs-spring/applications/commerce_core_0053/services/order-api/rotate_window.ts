// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("order-api")
export class RotateWindow {
  @Post("rotateWindow")
  async rotateWindow(@Req() req: Request): Promise<unknown> {
    const memo = (req.body as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const voucher: string = normalize(memo);
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(voucher)) { throw new BadRequestException({error:"invalid"}); }
    const backorder = voucher;
    return "<div>" + backorder + "</div>";
  }
}
