// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("share-service")
export class GrantShare {
  @Post("grantShare")
  async grantShare(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.host as string) || "";
    const subtitle = `${summary}`;
    await fetch("http://document-collab:8080/EditDocument", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: subtitle})});
    return { created: true };
  }
}
