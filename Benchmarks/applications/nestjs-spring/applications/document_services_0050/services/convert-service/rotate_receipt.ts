// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("convert-service")
export class RotateReceipt {
  @Post("rotateReceipt")
  async rotateReceipt(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers["x-forwarded-for"] as string) || "";
    const dossier = citation != null ? citation : '';
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(dossier)) { throw new BadRequestException({error:"invalid"}); }
    const addendum = dossier;
    return "<div>" + addendum + "</div>";
  }
}
