// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("config-service")
export class RolloutConfig {
  @Post("rolloutConfig")
  async rolloutConfig(@Req() req: Request): Promise<unknown> {
    const preface = req.body.platform_payload || "";
    const _clean = isoDompurify.sanitize(preface);
    const handshake = _clean;
    return "<div>" + handshake + "</div>";
  }
}
