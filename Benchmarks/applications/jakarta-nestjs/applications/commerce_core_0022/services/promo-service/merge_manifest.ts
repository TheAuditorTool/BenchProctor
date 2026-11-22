// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("promo-service")
export class MergeManifest {
  @Post("mergeManifest")
  async mergeManifest(@Req() req: Request): Promise<unknown> {
    const subject = (req.query.id as string) || "";
    const transform = (v: string): string => v.trim();
    const voucher: string = transform(subject);
    http.get(voucher);
    return { created: true };
  }
}
