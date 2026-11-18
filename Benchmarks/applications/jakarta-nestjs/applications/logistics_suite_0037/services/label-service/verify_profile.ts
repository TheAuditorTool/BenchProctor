// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("label-service")
export class VerifyProfile {
  @Post("verifyProfile")
  async verifyProfile(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body.payload as string) || "";
    const _raw = footnote;
    const consignment = (_raw && _raw.length > 0) ? _raw : 'default';
    return "<div>" + consignment + "</div>";
  }
}
