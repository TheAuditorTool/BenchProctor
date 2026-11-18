// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("promo-service")
export class CollectManifest {
  @Post("collectManifest")
  async collectManifest(@Req() req: Request): Promise<unknown> {
    const heading = (req.headers.authorization as string) || "";
    const voucher = Buffer.from(heading, "base64").toString();
    return "<div>" + voucher + "</div>";
  }
}
