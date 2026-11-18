// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post, BadRequestException } from "@nestjs/common";
import { Response } from "express";
import * as ldapjs from "ldapjs";
import * as zod from "zod";
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
  @Post("BenchmarkTest00651")
  async BenchmarkTest00651(@Body("multipart_field") mf: string): Promise<unknown> {
    const userInput = mf || "";
    const data = String(userInput).split(/[ \t]+/).join(" ");
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.#%\-]+$/).safeParse(String(data));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const processed = _parsed.data;
    const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
    ldapClient.on("error", () => {});
    ldapClient.search("ou=people,dc=example,dc=com", { filter: "(uid=" + processed + ")", scope: "sub" }, (_err, _res) => (_res ? _res.on("end", () => ldapClient.unbind()).on("error", () => ldapClient.unbind()) : ldapClient.unbind()));
    return { created: true };
  }
}
