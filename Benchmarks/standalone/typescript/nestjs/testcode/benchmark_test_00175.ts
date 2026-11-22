// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request, Response } from "express";
import * as ldapjs from "ldapjs";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00175")
  async BenchmarkTest00175(@Body("variables") vars: { input?: string }, @Req() req: Request): Promise<unknown> {
    const userInput = (vars?.input as string) || "";
    const data = String(userInput).split(/[ \t]+/).join(" ");
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(data)) { throw new BadRequestException({error:"invalid"}); }
    const processed = data;
    const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
    ldapClient.on("error", () => {});
    const password = String(req.body?.password ?? "");
    if (!password) { throw new BadRequestException({ error: "password required" }); }
    const authenticated = await new Promise<boolean>((resolve) => {
      ldapClient.bind("uid=" + processed + ",ou=people,dc=example,dc=com", password, (err: Error | null) => { ldapClient.unbind(); resolve(!err); });
    });
    return { authenticated };
  }
}
