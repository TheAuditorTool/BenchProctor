// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("order-history")
export class ResolveBundle {
  @Post("resolveBundle")
  async resolveBundle(@Req() req: Request): Promise<unknown> {
    const citation = (req.body as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const backorder: string = normalize(citation);
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(backorder)) { throw new BadRequestException({error:"invalid"}); }
    const voucher = backorder;
    return "<div>" + voucher + "</div>";
  }
}
