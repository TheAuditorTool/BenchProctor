// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("metadata-index")
export class RotateReceipt {
  @Post("rotateReceipt")
  async rotateReceipt(@Req() req: Request): Promise<unknown> {
    const citation = process.env.MEDIA_INPUT_0028 || "";
    const transform = (v: string): string => v.trim();
    const rendition: string = transform(citation);
    if (!/^(asc|desc|name|created)$/.test(String(rendition))) { throw new BadRequestException({error:"invalid"}); }
    const montage = rendition;
    await db.query("SELECT * FROM users ORDER BY " + montage);
    return { created: true };
  }
}
