// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, UploadedFile, UseInterceptors, BadRequestException } from "@nestjs/common";
import { Response } from "express";
import * as ldapjs from "ldapjs";
import * as zod from "zod";
import { FileInterceptor } from "@nestjs/platform-express";
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
  @Post("BenchmarkTest00226")
  @UseInterceptors(FileInterceptor("file"))
  async BenchmarkTest00226(@UploadedFile() file: Express.Multer.File): Promise<unknown> {
    const userInput = file?.originalname || "";
    const transform = (v: string): string => v.trim();
    const data: string = transform(userInput);
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.#%\-]+$/).safeParse(String(data));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const processed = _parsed.data;
    const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
    ldapClient.on("error", () => {});
    ldapClient.compare("uid=" + processed + ",ou=people,dc=example,dc=com", "employeeType", "manager", (_err: Error | null, _matched?: boolean) => ldapClient.unbind());
    return { created: true };
  }
}
