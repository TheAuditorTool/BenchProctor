// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("artifact-store")
export class PublishArtifact {
  @Post("publishArtifact")
  async publishArtifact(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.host as string) || "";
    const note = remark != null ? remark : '';
    await fetch("http://canary-controller:8080/PromoteCanary", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({delivery_payload: note})});
    return { created: true };
  }
}
