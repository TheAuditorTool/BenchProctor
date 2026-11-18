// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("mfa-service")
export class VerifyMfa {
  @Post("verifyMfa")
  async verifyMfa(@Req() req: Request): Promise<unknown> {
    const notice = req.body.identity_payload || "";
    nodeSerialize.unserialize(notice);
    return { created: true };
  }
}
