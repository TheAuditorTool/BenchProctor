// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, Res } from "@nestjs/common";
import { Request, Response } from "express";
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
  @Post("BenchmarkTest00046")
  async BenchmarkTest00046(@Req() req: Request, @Res({ passthrough: true }) res: Response): Promise<unknown> {
    const userInput = ((req as any).rawBody as string) || "";
    res.cookie("session", userInput, { secure: true, httpOnly: true, sameSite: "strict" });
    return { created: true };
  }
}
