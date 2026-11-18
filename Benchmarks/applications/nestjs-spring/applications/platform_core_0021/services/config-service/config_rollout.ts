// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("config-service")
export class RolloutConfig {
  @Post("rolloutConfig/:id")
  async rolloutConfig(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.params.id as string) || "";
    const handshake = decodeURIComponent(excerpt);
    await fetch("http://platform-api:8080/ProvisionTenant", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: handshake})});
    return { created: true };
  }
}
