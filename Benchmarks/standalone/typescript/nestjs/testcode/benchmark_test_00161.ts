// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post, Res } from "@nestjs/common";
import { Response } from "express";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";
import { stringifySetCookie } from "cookie";

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
  @Post("BenchmarkTest00161")
  async BenchmarkTest00161(@Headers("authorization") auth: string, @Res({ passthrough: true }) res: Response): Promise<unknown> {
    const userInput = auth || "";
    res.append(
      "Set-Cookie",
      stringifySetCookie({ name: "session", value: String(userInput), path: "/", httpOnly: true, sameSite: "strict" }),
    );
    return { created: true };
  }
}
