// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("signature-verifier")
export class ValidateProfile {
  @Post("validateProfile")
  async validateProfile(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.body as string) || "";
    const handshake = String(synopsis).split(/[ \t]+/).join(" ");
    http.get(handshake);
    return { created: true };
  }
}
